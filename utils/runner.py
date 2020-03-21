import os
import api
import glob

from utils.register import Register


class Runner(object):
    def __init__(self, register:Register=None, face_folder:str=None,
                 test:bool=False, clear:bool=False):
        self.register = register
        self.face_folder = face_folder
        self.clear = clear
        self.test = test

    def run(self):
        if self.clear:
            self.register.clear()
        if self.face_folder is not None:
            if self.test:
                return self._run_test()
            else:
                return self._run_register()

    def _run_register(self):
        """Register register's face encoding into data base
        Parameters:
            register: data base handler
            face_folder: image file folder
        Returns:

        """
        import re
        for img in glob.glob(os.path.join(self.face_folder, "*.jpg")):
            name = re.split('[./]', img)[-2]
            encoding = api.face_encodings(api.load_image_file(img))[0]

            ret, msg = self.register.insert_query(name, str(encoding.tolist()))
            if not ret:
                return f'Register {img} Error, Msg: {msg}'
        else:
            return ('Register successed')

    def _run_test(self):
        """
        face recognition
        :param register: data base handler
        :param face_folder: image file folder
        :return: recognize result
        """
        know_encodings = self.register.get_encodings()
        res = {}
        for img in glob.glob(os.path.join(self.face_folder, "*.jpg")):
            # Load a test image and get face enconding
            image_to_test = api.load_image_file(img)
            image_to_test_encoding = api.face_encodings(image_to_test)[0]
            test_res = []
            for id, (name, encoding) in know_encodings.items():

                face_ret = api.compare_faces(encoding, image_to_test_encoding, tolerance=0.42)
                if face_ret:
                    test_res += [name]
            if len(test_res) > 0:
                # return(f'Face Recognition successed, {img} is {test_res}')
                res[img] = test_res
            else:
                # return(f'Face {img} Recognition failed, please try again !!!')
                res[img] = None
        return res
