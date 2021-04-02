FIRST	LDA	#256		.100을 로드(hex256=dec100). 스택포인터의 시작주소.
	JSUB	STINIT		.스택초기화.
	LDX	ZERO		.레지스터X에 0로드.
	LDA	ZERO		.레지스터A에 0로드.
	STA	RESULT		.RESULT에 0 저장.

CALLK	LDX	ZERO		.레지스터X에 0로드.
	TD	INDEV		.test DEVICE
	JEQ	CALLK		.DEVICE가 준비가 않되면 '같음'을 CC에 저장. JEQ는 CC가 '같음'이면 수행. 
	RD	INDEV		.DEVICE로 부터 값을 받음. (=scanf)
	COMP	NLC		.입력받은 값을 NLC와 비교함. 10보다 크다->OUTLP, 작다 OUTLP2
	JEQ	CALLK		.입력받은 값이 10이라면 CALLK 다시 감.
	SUB	#48		.입력받은 값에 -48. 숫자로 저장하려고 빼줌. CHAR 49는 숫자 1. 아스키코드 참고.
	STA	KK		.계산 된 숫자 값 KK에 저장.

INLOOP	TD	INDEV		.test DEVICE
	JEQ	INLOOP		.DEVICE가 준비가 않되면 '같음'을 CC에 저장. JEQ는 CC가 '같음'이면 수행. 
	RD	INDEV		.DEVICE로 부터 값을 받음. (=scanf)
	COMP	NLC		.입력받은 값을 NLC와 비교함. 10보다 크다->OUTLP, 작다 OUTLP2
	JEQ	INLOOP		.입력받은 값이 10이라면 INLOOP 다시 감.
	COMP	ZEROCH		.입력받은 값이 ZERO인지 체크. 아스키코드 참고, CHAR 48 = 숫자 0
	JEQ	ZCASE		.입력받은 값이 ZERO라면, ZCASE로 감.
	SUB	#48		.입력받은 값에 -48. 숫자로 저장하려고 빼줌. CHAR 49는 숫자 1. 아스키코드 참고 .
	STA	TMP		.계산 된 숫자 값 TMP에 저장.
	JSUB	PUSH		.PUSH 호출.
	LDA	TMP		.TMP를 레지스터A에 로드.
	ADD	RESULT		.결과에 더함. 
	STA	RESULT		.결과를 저장.

CHECK	LDA	ZERO		.레지스터X에 0로드.
	TIX	KK		.레지스터X값을 1 증가시킨 후 KK값과 비교하여 결과를 CC에 저장. (작음,같음,큼)
	JLT	INLOOP		.CC값이 작음이면 INLOOP로 감.
	JEQ	OUTLP		.CC값이 같음이면 OUTLP로 감.

ZCASE	JSUB	POP		.POP 호출.
	STA	TMP		.레지스터A값 TMP에 저장.
	LDA	RESULT		.레지스터A에 RESULT 로드.  
	SUB	TMP		.
	STA	RESULT		.레지스터A값 REULST에 저장.
	J	CHECK		.CHECK로 감.

OUTLP	TD	OUTDEV		.test DEVICE
	JEQ	OUTLP		.DEVICE가 준비가 않되면 '같음'을 CC에 저장. JEQ는 CC가 '같음'이면 수행. 
	LDA	RESULT		.레지스터A에 RESULT 로드.
	COMP	#10		.레지스터A값 10과 비교. ( RESULT ? 10 )
	JLT	OUTLP2		.10보다 작으면 OUTLP2로 감.
	DIV	#10		.레지스터A값 10으로 나눔. RESULT / 10 
	MUL	#10		.레지스터A값에 10 곱함.  (RESULT / 10) * 10 
	STA	TMP		.레지스터A값을 TMP에 저장.
	DIV	#10		.레지스터A값 10으로 나눔. ((RESULT / 10) * 10 ) / 10
	ADD	#48		.레지스터A값에 48더함.   ((RESULT / 10) * 10 ) / 10 + 48
	WD	OUTDEV		.레지스터A값 출력
	LDA	RESULT		.레지스터A에 RESULT 로드.
	SUB	TMP		.RESULT = RESULT - TMP

OUTLP2	ADD	#48		.레지스터A값에 48을 더함
	WD	OUTDEV		.레지스터A값 출력
	J	FIN		.FIN으로 감. 끝.

STINIT	STA	STACKPTR	.256을 STACKPTR에 저장
	RSUB			.서브루틴 끝. 돌아감.

PUSH	STA	@STACKPTR	.레지스터A값 STACKPTR의 주소값이 가리키는 곳에 저장.
	LDA	STACKPTR	.STACKPTR 주소값 로드.
	ADD	#3		.STACKPTR 주소값 + 3, WORD는 주소크기가 3이다.
	STA	STACKPTR	.주소 STACKPTR 저장.
	RSUB			.서브루틴 끝. 돌아감.

POP	LDA	STACKPTR	.STACKPTR 주소값 로드
	SUB	#3		.STACKPTR 주소값 - 3
	STA	STACKPTR	.STACKPTR에 저장.
	LDA	@STACKPTR	.STACKPTR 주소값이 참조하는 값 로드.
	RSUB			.서브루틴 끝. 돌아감.

FIN
	END	FIRST

INDEV	BYTE	0
OUTDEV	BYTE	1
ZERO	BYTE	0
TMP	RESW	1
KK	RESW	1
RESULT	RESW	1
NLC	WORD	10
ZEROCH	WORD	48

STACKPTR	RESW	1