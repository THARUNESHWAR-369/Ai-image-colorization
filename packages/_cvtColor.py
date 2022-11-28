
import numpy as np
import cv2
import os

from ._imgConverter import IMG_CONVERTER

class COLORIZE(IMG_CONVERTER):

    __PROTOTXT_MODEL_PATH = "models/colorization_deploy_v2.prototxt"
    __COFFE_MODEL_PATH = "models/colorization_release_v2.caffemodel"
    __POINTS_MODEL_PATH = os.path.join("models", "pts_in_hull.npy")
  
    def start_process(self, image_data):
        net = cv2.dnn.readNetFromCaffe(self.__PROTOTXT_MODEL_PATH, self.__COFFE_MODEL_PATH)
        pts = np.load(self.__POINTS_MODEL_PATH)
        class8 = net.getLayerId("class8_ab")
        conv8 = net.getLayerId("conv8_313_rh")
        pts = pts.transpose().reshape(2, 313, 1, 1)
        net.getLayer(class8).blobs = [pts.astype("float32")]
        net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]
        
        try:
            image = image_data
            
            print("Image loaded successful")
            
            scaled = image.astype("float32") / 255.0
            
            print("image Scaled successful")
            lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)

            resized = cv2.resize(lab, (224, 224))
            L = cv2.split(resized)[0]
            L -= 50

            net.setInput(cv2.dnn.blobFromImage(L))
            ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
            ab = cv2.resize(ab, (image.shape[1], image.shape[0]))

            L = cv2.split(lab)[0]
            
            print("successful completed upto L")
            
            colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
            
            print("successful completed upto colorized (1)")
            colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
            colorized = np.clip(colorized, 0, 1)
            print("successful completed upto colorized (2)")
            colorized = (255 * colorized).astype("uint8")
            print("successful completed upto colorized (3)")

            return True, self.numpyArrayToBytesIO(colorized)
            
        except Exception as e:
            print("c2.imread:(Excpet) ", e)
            return False, None
