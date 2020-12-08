from DrivingInterface.drive_controller import DrivingController

class DrivingClient(DrivingController):
    def __init__(self):
        # =========================================================== #
        #  Area for member variables =============================== #
        # =========================================================== #
        # Editing area starts from here
        #

        self.is_debug = False

        # api or keyboard
        self.enable_api_control = True # True(Controlled by code) /False(Controlled by keyboard)
        super().set_enable_api_control(self.enable_api_control)

        #
        # Editing area ends
        # ==========================================================#
        super().__init__()
    
    def control_driving(self, car_controls, sensing_info):

        # =========================================================== #
        # Area for writing code about driving rule ================= #
        # =========================================================== #
        # Editing area starts from here
        #

        if self.is_debug:
            print("=========================================================")
            print("[MyCar] to middle: {}".format(sensing_info.to_middle))

            print("[MyCar] collided: {}".format(sensing_info.collided))
            print("[MyCar] car speed: {} km/h".format(sensing_info.speed))

            print("[MyCar] is moving forward: {}".format(sensing_info.moving_forward))
            print("[MyCar] moving angle: {}".format(sensing_info.moving_angle))
            print("[MyCar] lap_progress: {}".format(sensing_info.lap_progress))

            print("[MyCar] track_forward_angles: {}".format(sensing_info.track_forward_angles))
            print("[MyCar] track_forward_obstacles: {}".format(sensing_info.track_forward_obstacles))
            print("[MyCar] opponent_cars_info: {}".format(sensing_info.opponent_cars_info))
            print("[MyCar] distance_to_way_points: {}".format(sensing_info.distance_to_way_points))
            print("=========================================================")

        ###########################################################################

        set_throttle = 0.98
        set_brake = 0

        # 현재 속도에 따라 몇 미터앞의 커브값을 가져올 지 계산한다
        # 빠를수록 더 먼거리의 각도를 미리 가져온다.
        angle_num = int(sensing_info.speed / 45)
        ref_angle = sensing_info.track_forward_angles[angle_num]

        # 중앙선 기준 차량 위치에 따른 핸들값
        middle_add = (sensing_info.to_middle / 70) * - 1

        # 전방의 커브값에 내 차량의 각도를 빼면 핸들을 틀어야할 값 속도에 따른 비율로 나눠준다.
        set_steering = (ref_angle - sensing_info.moving_angle) / (230 - sensing_info.speed)

        # 부드럽게 주행 가능, 도로 중앙을 따라 주행 가능
        set_steering += middle_add

        car_controls.steering = set_steering
        car_controls.throttle = set_throttle
        car_controls.brake = set_brake


        if self.is_debug:
            print("[MyCar] steering:{}, throttle:{}, brake:{}"\
                  .format(car_controls.steering, car_controls.throttle, car_controls.brake))
        # Editing area ends
        # ==========================================================#
        return car_controls


    # ============================
    # If you have NOT changed the <settings.json> file
    # ===> player_name = ""
    #
    # If you changed the <settings.json> file
    # ===> player_name = "My car name" (specified in the json file)  ex) Car1
    # ============================
    def set_player_name(self):
        player_name = ""
        return player_name


if __name__ == '__main__':
    print("[MyCar] Start Bot! (PYTHON)")

    client = DrivingClient()
    return_code = client.run()

    print("[MyCar] End Bot! (PYTHON)")

    exit(return_code)
