import re
import aiohttp
import asyncio

async def get_matrix(url: str) -> [int]:
    async with aiohttp.ClientSession() as session:
        async with session.get(SOURCE_URL) as response:
            if response.status != 200:
                raise Exception(f'Status code error: {page.status_code}')
            else:
                matrix = await response.text()
        
    nums = re.findall(r'\d+', matrix)
    len_arr = len(re.findall(r'\d+ \|\n', matrix))

    matr = []
    for i in range(0, len_arr**2, len_arr):
        matr.append(nums[i:i+len_arr])

    len_arr = len(matr)
    line = []
    for c in range(len_arr//2):
        #левый столбец
        for i in range(c, len_arr-c):
            line.append(int(matr[i][c]))

        # нижняя строка
        for i in range(c+1, len_arr-c):
            line.append(int(matr[-c-1][i]))

        # правый столбец
        for i in range(len_arr-c-2, c-1, -1):
            line.append(int(matr[i][-c-1]))

        #верхняя строка
        for i in range(len_arr-c-2, c, -1):
            line.append(int(matr[c][i]))

    if len_arr % 2 != 0:
        line.append(int(matr[len_arr//2][len_arr//2]))

    return line

def test_get_matrix():
    assert asyncio.run(get_matrix(SOURCE_URL)) == TRAVERSAL

if __name__ == '__main__':
    SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
    TRAVERSAL = [
        10, 50, 90, 130,
        140, 150, 160, 120,
        80, 40, 30, 20,
        60, 100, 110, 70
        ]
    test_get_matrix()

