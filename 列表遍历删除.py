bullets = [1,2,3,4,0,-1,-1,-2,-3]
for it in bullets:
    if it < 0:
        bullets.remove(it)

print(bullets)
