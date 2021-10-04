from imageai.Prediction.Custom import CustomImagePrediction
import os
def executable():
    execution_path = os.getcwd()

    prediction = CustomImagePrediction()
    prediction.setModelTypeAsResNet()
    prediction.setModelPath("model_ex-148_acc-0.843750.h5")
    prediction.setJsonPath("model_class.json")
    prediction.loadModel(num_objects=8)

    predictions, probabilities = prediction.predictImage('cofimage.jpg', result_count=1)

    crop=""
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        crop += str(eachPrediction)
    
    return crop
    
    
#executable()
