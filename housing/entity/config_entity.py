from collections import namedtuple


DataInjestionConfig = namedtuple("DataInjestionConfig",
                                 ["dataset_download_url",
                                  "raw_data_dir",
                                  "injested_train_dir",
                                  "injested_test_dir"
                                  ])


DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig",
                                      ["add_bedroom_per_room",
                                       "transformed_train_dir",
                                       "transformed_test_dir",
                                       "preprocessed_object_file_path"])


ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["trained_model_file_path",
                                                       "base_accuracy"])


ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path",
                                                             "time_stamp"])


ModelPusherConfg = namedtuple("ModelPusherConfig",["export_dir_path"])


TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])