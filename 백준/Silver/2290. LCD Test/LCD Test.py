s,n=map(int,input().split())
n=str(n)
n=list(n)

for k in range(2*s+3):
    h=''
    for j in n:
        if j=='4':
            popo=34
        #가로 그릴 거임
        if k==0 or k==2*s+3-1 or k==(2*s+3)//2:
            if j=='1' or j=='2' or j=='3' or j=='5' or j=='6' or j=='8' or j=='9' or j=='0' :
                if j=='1':
                    for ll in range(s + 2):
                        h += ' '
                elif j=='0' and k==(2*s+3)//2:
                    for ll in range(s+2):

                            h+=' '
                else:
                    for ll in range(s+2):
                        if ll==0 or ll==s+1:
                            h+=' '
                        else:
                            h+='-'
            elif j=='4':
                if k==(2*s+3)//2:
                    for ll in range(s + 2):
                        if ll == 0 or ll == s + 1:
                            h += ' '
                        else:
                            h += '-'
                else:
                    for ll in range(s + 2):

                            h += ' '
            elif j=='7':
                if k==0:
                    for ll in range(s + 2):
                        if ll == 0 or ll == s + 1:
                            h += ' '
                        else:
                            h += '-'
                else:
                    for ll in range(s + 2):
                        h += ' '
            h+=' '
        #세로 그리기
        else:
            if j=='1':
                for ll in range(s + 2):
                    if ll == s + 1:
                        h += '|'
                    else:
                        h += ' '
            elif j=='2':
                if  k<(2*s+3)//2:
                    for ll in range(s + 2):
                        if ll == s + 1:
                            h += '|'
                        else:
                            h += ' '
                elif k>(2*s+3)//2:
                    for ll in range(s + 2):
                        if ll == 0:
                            h += '|'
                        else:
                            h += ' '
            elif j=='3':
                for ll in range(s + 2):
                        if ll == s + 1:
                            h += '|'
                        else:
                            h += ' '
            elif j=='4':
                if  k<(2*s+3)//2:
                    for ll in range(s + 2):
                        if ll == s + 1 or ll==0:
                            h += '|'
                        else:
                            h += ' '
                elif k>(2*s+3)//2:
                    for ll in range(s + 2):
                        if ll == s+1:
                            h += '|'
                        else:
                            h += ' '
            elif j=='5':
                if  k>(2*s+3)//2:
                    for ll in range(s + 2):
                        if ll == s + 1:
                            h += '|'
                        else:
                            h += ' '
                elif k<(2*s+3)//2:
                    for ll in range(s + 2):
                        if ll == 0:
                            h += '|'
                        else:
                            h += ' '
            elif j=='6':
                if  k>(2*s+3)//2:
                    for ll in range(s + 2):
                        if ll == s + 1 or ll==0:
                            h += '|'
                        else:
                            h += ' '
                elif k<(2*s+3)//2:
                    for ll in range(s + 2):
                        if ll == 0:
                            h += '|'
                        else:
                            h += ' '
            elif j=='7':
                for ll in range(s + 2):
                        if ll == s+1:
                            h += '|'
                        else:
                            h += ' '
            elif j=='8' or j=='0':
                for ll in range(s + 2):
                        if ll == s+1 or ll==0:
                            h += '|'
                        else:
                            h += ' '
            elif j == '9':
                if  k>(2*s+3)//2:
                    for ll in range(s + 2):
                        if ll == s + 1 :
                            h += '|'
                        else:
                            h += ' '
                elif k<(2*s+3)//2:
                    for ll in range(s + 2):
                        if ll == 0 or ll==s+1:
                            h += '|'
                        else:
                            h += ' '
            h+=' '
    print(h)