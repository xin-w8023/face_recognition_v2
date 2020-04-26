import PIL.Image
import dlib
import numpy as np
import pretrained_models

# face detector in dlib
face_detector = dlib.get_frontal_face_detector()
cnn_face_detector = dlib.cnn_face_detection_model_v1(pretrained_models.cnn_face_detector_model_location())

# load pretrained model (to get face landmarks)
predictor_5_point_model = pretrained_models.pose_predictor_five_point_model_location()
predictor_68_point_model = pretrained_models.pose_predictor_model_location()

# given face landmarks, crop face area
pose_predictor_5_point = dlib.shape_predictor(predictor_5_point_model)
pose_predictor_68_point = dlib.shape_predictor(predictor_68_point_model)

# load pretrained face recognition model
face_recognition_model = pretrained_models.face_recognition_model_location()
face_encoder = dlib.face_recognition_model_v1(face_recognition_model)


def load_image_file(img_file, mode='RGB'):
    """
    Loads an image file (.jpg, .png, etc) into a numpy array
    Parameters:
        img_file (Path): image file to load
        mode: format to convert the image to. Only 'RGB' (8-bit RGB, 3 channels) and
              'L' (black and white) are supported.
    Returns:
        image contents as numpy array
    """
    img = PIL.Image.open(img_file)
    if mode:
        img = img.convert(mode)
    return np.array(img)

def coord_to_rect(coord):
    """
    Convert a tuple in (top, right, bottom, left) order to a dlib `rect` object
    Parameters:
        coord (tuple):  plain tuple representation of the rect in (top, right, bottom, left) order
    Returns:
        a dlib `rect` object
    """
    return dlib.rectangle(coord[3], coord[0], coord[1], coord[2])

def get_face_locations(img, number_of_times_to_upsample=1, model='cnn'):
    """
    Returns an array of bounding boxes of human known_faces in a image
    Parameters:
        img (ndarray): An image (as a numpy array)
        number_of_times_to_upsample (int): How many times to upsample the image looking for known_faces.
                                           Higher numbers find smaller known_faces.

    Returns:
        A list of dlib 'rect' objects of found face locations
    """
    if model == "cnn":
        return [item.rect for item in cnn_face_detector(img, number_of_times_to_upsample)]
    else:
        return face_detector(img, number_of_times_to_upsample)

def _raw_face_landmarks(face_image, model='cnn', face_locations=None):
    if face_locations is None:
        face_locations = get_face_locations(face_image, model=model)
    else:
        if model == 'cnn':
            face_locations = [coord_to_rect(face_location.rect) for face_location in face_locations]
        else:
            face_locations = [coord_to_rect(face_location) for face_location in face_locations]

    pose_predictor = pose_predictor_68_point
    return [pose_predictor(face_image, face_location) for face_location in face_locations]


def face_encodings(face_image, model='cnn', known_face_locations=None, num_jitters=1):
    """
    Given an image, return the 128-dimension face encoding for each face in the image.
    Parameters:
        face_image: The image that contains one or more known_faces
        known_face_locations: Optional - the bounding boxes of each face if you already know them.
        num_jitters: How many times to re-sample the face when calculating encoding. Higher is more
                     accurate, but slower (i.e. 100 is 100x slower)
    Returns:
         A list of 128-dimensional face encodings (one for each face in the image)
    """
    raw_landmarks = _raw_face_landmarks(face_image, model=model, face_locations=known_face_locations)
    return [np.array(face_encoder.compute_face_descriptor(face_image, raw_landmark_set, num_jitters))
            for raw_landmark_set in raw_landmarks]

def face_distance(face_encodings, face_to_compare):
    """
    Given a list of face encodings, compare them to a known face encoding and get a euclidean distance
    for each comparison face. The distance tells you how similar the known_faces are.
    Parameters:
        known_faces (List(ndarray)): List of face encodings to compare
        face_to_compare (ndarray): A face encoding to compare against
    Returns:
        A numpy ndarray with the distance for each face in the same order as the 'known_faces' array
    """
    if len(face_encodings) == 0:
        return np.empty((0))

    return np.linalg.norm(face_encodings - face_to_compare, axis=1)

def compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.4):
    """
    Compare a list of face encodings against a candidate encoding to see if they match.
    Parameters:
        known_face_encodings: A list of known face encodings
        face_encoding_to_check: A single face encoding to compare against the list
        tolerance: How much distance between known_faces to consider it a match. Lower is more strict.
                   0.6 is typical best performance.
    Returns:
        A list of True/False values indicating which known_face_encodings match the face encoding to check
    """

    distance = face_distance(known_face_encodings, face_encoding_to_check)
    return  distance <= tolerance, distance