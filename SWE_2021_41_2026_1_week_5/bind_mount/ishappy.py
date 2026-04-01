def isHappy(n):
    if n < 1 or n > 2**31 - 1:
        return False
    Set = set()
    while n != 1 and n not in Set:
        Set.add(n)
        n = sum(int(d) ** 2 for d in str(n))

    return n == 1

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)

    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")

    print("Results saved to /app/bind_mount/output.txt")