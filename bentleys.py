array = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

m = 0
m_array = []

for i in array:
    sum = 0

    while j in range(i, len(array)):

        sum += array[j]
        if sum > m:
            m = sum
            m_array = array[i:j]
        j += 1
print(m, m_array)
