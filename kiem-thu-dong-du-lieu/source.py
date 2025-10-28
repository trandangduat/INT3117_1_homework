def check_robot_status(R, C, energy, obstacles):
    """
    Kiểm tra trạng thái robot dọn nhà.

    R, C      : vị trí hiện tại của robot (hàng, cột)
    energy    : năng lượng hiện tại của robot (0 -> 100)
    obstacles : danh sách các vị trí vật cản dạng list of tuples [(r1,c1), (r2,c2), ...]
    """

    if R < 1 or R > 5 or C < 1 or C > 7:
        return "NOT OK"

    if 1 <= R <= 2 and 4 <= C <= 7:
        return "NOT OK"

    i = 0
    while i < len(obstacles):
        if (energy < 10):
            return "NEED CHARGING"

        energy -= 10
        if obstacles[i][0] == R and obstacles[i][1] == C:
            return "NOT OK"
        i += 1


    return "OK"
