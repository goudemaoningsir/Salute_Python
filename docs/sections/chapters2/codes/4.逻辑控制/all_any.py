def all_numbers_gt_10_2(numbers):
    return bool(numbers) and all(n > 10 for n in numbers)


print(all_numbers_gt_10_2([11, 20, 30]))
print(all_numbers_gt_10_2([1, 20, 30]))
