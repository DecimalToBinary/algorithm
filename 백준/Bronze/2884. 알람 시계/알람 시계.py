H,M = map(int,input().split())

if M<45:
    if H==0:
        print(f'23 {60-(45-M)}')
    else:
        print(f'{H-1} {60-(45-M)}')
else:
    print(f'{H} {M-45}')