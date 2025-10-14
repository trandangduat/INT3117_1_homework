def check_robot_cleaning(R, C, obstacles):
    """
    Kiểm tra xem robot có đang dọn nhà hay không.

    Tham số:
        R (int): vị trí hàng (1–5)
        C (int): vị trí cột (1–7)
        obstacles (list[tuple[int, int]]): danh sách chướng ngại vật [(r1,c1), (r2,c2), ...]

    Trả về:
        str: "OK" nếu robot đang dọn nhà, "NOT OK" nếu không.
    """

    if R < 1 or R > 5 or C < 1 or C > 7:
        return "NOT OK"

    if 1 <= R <= 2 and 4 <= C <= 7:
        return "NOT OK"

    for i in range(len(obstacles)):
        r_obs, c_obs = obstacles[i]
        if R == r_obs and C == c_obs:
            return f"NOT OK"

    return "OK"
