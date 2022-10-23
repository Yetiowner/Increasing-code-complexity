"""
A 10x Hello World in a pure-Python Python bytecode interpreter.
Based on https://github.com/nedbat/byterun adjusted to run in a single file!
No need for documentation the code explain itself
$ python3 complication.py 

<code object <module> at 0x7fd6cda9aa20, file "main.py", line 1>
  1           0 LOAD_CONST               0 ('Hello World!\n')
              2 STORE_NAME               0 (HW)

  2           4 LOAD_NAME                1 (print)
              6 LOAD_NAME                0 (HW)
              8 LOAD_NAME                2 (len)
             10 LOAD_NAME                0 (HW)
             12 CALL_FUNCTION            1
             14 LOAD_CONST               1 (3)
             16 BINARY_SUBTRACT
             18 BINARY_MULTIPLY
             20 CALL_FUNCTION            1
             22 POP_TOP
             24 LOAD_CONST               2 (None)
             26 RETURN_VALUE
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!

"""

from __future__ import print_function,division
AQ='XOR'
AP='AND'
AO='RSHIFT'
AN='LSHIFT'
AM='SUBTRACT'
AL='ADD'
AK='MODULO'
AJ='TRUE_DIVIDE'
AI='FLOOR_DIVIDE'
AH='DIVIDE'
AG='MULTIPLY'
AF='POWER'
AE="name '%s' is not defined"
AD='with'
AC='break'
AB='    '
AA='__builtins__'
A9='__doc__'
A8='__dict__'
A7='__name__'
A6=slice
A5=range
A4=hasattr
s='silenced'
r='setup-except'
q='loop'
p=True
o=NameError
n=Exception
m=StopIteration
f=''
e='reraise'
d='yield'
c=dict
b=zip
Z='finally'
Y=str
X=getattr
W=TypeError
V=tuple
R='return'
Q='continue'
P='except-handler'
O=BaseException
N=issubclass
M=print
J=len
H='exception'
F=type
C=isinstance
A=None
import dis as G,inspect as t,linecache as g,logging as h,operator as B,sys as D,types as S,textwrap as u,six as I
from six.moves import reprlib as v
E,K=I.PY3,not I.PY3
'Implementations of Python fundamental objects for Byterun.'
import collections as w,re
def x(value):
	A=(lambda x:lambda:x)(value)
	if E:return A.__closure__[0]
	else:return A.func_closure[0]
class T:
	__slots__=['func_code','func_name','func_defaults','func_globals','func_locals','func_dict','func_closure',A7,A8,A9,'_vm','_func']
	def __init__(B,name,code,globs,defaults,kwdefaults,closure,vm):
		H=defaults;G=globs;F=closure;C=code;B._vm=vm;B.func_code=C;B.func_name=B.__name__=name or C.co_name;B.func_defaults=H if E and D.version_info.minor>=6 else V(H);B.func_globals=G;B.func_locals=B._vm.frame.f_locals;B.__dict__={};B.func_closure=F;B.__doc__=C.co_consts[0]if C.co_consts else A;I={'argdefs':B.func_defaults}
		if F:I['closure']=V((x(0)for A in F))
		B._func=S.FunctionType(C,G,**I)
	def __repr__(A):return'<Function %s at 0x%08x>'%(A.func_name,id(A))
	def __get__(B,instance,owner):
		D=owner;C=instance
		if C is not A:return i(C,D,B)
		if K:return i(A,D,B)
		else:return B
	def __call__(A,*B,**D):
		if re.search('<(?:listcomp|setcomp|dictcomp|genexpr)>$',A.func_name):assert J(B)==1 and not D,'Surprising comprehension!';E={'.0':B[0]}
		else:E=t.getcallargs(A._func,*B,**D)
		C=A._vm.make_frame(A.func_code,E,A.func_globals,{},A.func_closure);H=32
		if A.func_code.co_flags&H:F=k(C,A._vm);C.generator=F;G=F
		else:G=A._vm.run_frame(C)
		return G
class i:
	def __init__(A,obj,_class,func):A.im_self=obj;A.im_class=_class;A.im_func=func
	def __repr__(B):
		C='%s.%s'%(B.im_class.__name__,B.im_func.func_name)
		if B.im_self is not A:return'<Bound Method %s of %s>'%(C,B.im_self)
		else:return'<Unbound Method %s>'%(C,)
	def __call__(B,*C,**D):
		if B.im_self is not A:return B.im_func(B.im_self,*C,**D)
		else:return B.im_func(*C,**D)
class j:
	"A fake cell for closures.\n\n    Closures keep names in scope by storing them not in a frame, but in a\n    separate object called a cell.  Frames share references to cells, and\n    the LOAD_DEREF and STORE_DEREF opcodes get and set the value from cells.\n\n    This class acts as a cell, though it has to jump through two hoops to make\n    the simulation complete:\n\n        1. In order to create actual FunctionType functions, we have to have\n           actual cell objects, which are difficult to make. See the twisty\n           double-lambda in __init__.\n\n        2. Actual cell objects can't be modified, so to implement STORE_DEREF,\n           we store a one-element list in our cell, and then use [0] as the\n           actual value.\n\n    "
	def __init__(A,value):A.contents=value
	def get(A):return A.contents
	def set(A,value):A.contents=value
y=w.namedtuple('Block','type, handler, level')
class z:
	def __init__(B,f_code,f_globals,f_locals,f_closure,f_back):
		H=f_closure;F=f_locals;E=f_back;C=f_code;B.f_code=C
		if D.version_info>=(3,4):B.opcodes=list(G.get_instructions(B.f_code))
		B.f_globals=f_globals;B.f_locals=F;B.f_back=E;B.stack=[]
		if E:B.f_builtins=E.f_builtins
		else:
			B.f_builtins=F[AA]
			if A4(B.f_builtins,A8):B.f_builtins=B.f_builtins.__dict__
		B.f_lineno=C.co_firstlineno;B.f_lasti=0;B.cells={}if C.co_cellvars or C.co_freevars else A
		for I in C.co_cellvars:B.cells[I]=j(B.f_locals.get(I))
		if C.co_freevars:assert J(C.co_freevars)==J(H);B.cells.update(b(C.co_freevars,H))
		B.block_stack=[];B.generator=A
	def __repr__(A):return'<Frame at 0x%08x: %r @ %d>'%(id(A),A.f_code.co_filename,A.f_lineno)
	def line_number(A):
		'Get the current line number the frame is executing.';B=A.f_code.co_lnotab;E=I.iterbytes(B[0::2]);F=I.iterbytes(B[1::2]);C=0;D=A.f_code.co_firstlineno
		for (G,H) in b(E,F):
			C+=G
			if C>A.f_lasti:break
			D+=H
		return D
class k:
	def __init__(A,g_frame,vm):B=False;A.gi_frame=g_frame;A.vm=vm;A.started=B;A.finished=B
	def __iter__(A):return A
	def next(B):return B.send(A)
	def send(B,value=A):
		C=value
		if not B.started and C is not A:raise W("Can't send non-None value to a just-started generator")
		B.gi_frame.stack.append(C);B.started=p;D=B.vm.resume_frame(B.gi_frame)
		if B.finished:raise m(D)
		return D
	__next__=next
log=h.getLogger(__name__)
if I.PY3:U=lambda b:b
else:U=ord
l=v.Repr()
l.maxother=120
a=l.repr
class L(n):'For raising errors in the operation of the VM.'
class A0:
	def __init__(B):B.frames=[];B.frame=A;B.return_value=A;B.last_exception=A
	def top(A):'Return the value at the top of the stack, with no changes.';return A.frame.stack[-1]
	def pop(A,i=0):'Pop a value from the stack.\n\n        Default to the top of the stack, but `i` can be a count from the top\n        instead.\n\n        ';return A.frame.stack.pop(-1-i)
	def push(A,*B):'Push values onto the value stack.';A.frame.stack.extend(B)
	def popn(A,n):
		'Pop a number of values from the value stack.\n\n        A list of `n` values is returned, the deepest value first.\n\n        '
		if n:B=A.frame.stack[-n:];A.frame.stack[-n:]=[];return B
		else:return[]
	def peek(A,n):'Get a value `n` entries down in the stack, without changing the stack.';return A.frame.stack[-n]
	def jump(A,jump):'Move the bytecode pointer to `jump`, so it will execute next.';A.frame.f_lasti=jump
	def push_block(C,type,handler=A,level=A):
		B=level
		if B is A:B=J(C.frame.stack)
		C.frame.block_stack.append(y(type,handler,B))
	def pop_block(A):return A.frame.block_stack.pop()
	def make_frame(D,code,callargs={},f_globals=A,f_locals=A,f_closure=A):
		E=callargs;C=f_locals;B=f_globals;log.info('make_frame: code=%r, callargs=%s'%(code,a(E)))
		if B is not A:
			B=B
			if C is A:C=B
		elif D.frames:B=D.frame.f_globals;C={}
		else:B=C={AA:__builtins__,A7:'__main__',A9:A,'__package__':A}
		C.update(E);F=z(code,B,C,f_closure,D.frame);return F
	def push_frame(A,frame):B=frame;A.frames.append(B);A.frame=B
	def pop_frame(B):
		B.frames.pop()
		if B.frames:B.frame=B.frames[-1]
		else:B.frame=A
	def print_frames(E):
		'Print the call stack, for debugging.'
		for A in E.frames:
			B=A.f_code.co_filename;C=A.line_number();M('  File "%s", line %d, in %s'%(B,C,A.f_code.co_name));g.checkcache(B);D=g.getline(B,C,A.f_globals)
			if D:M(AB+D.strip())
	def resume_frame(C,frame):B=frame;B.f_back=C.frame;D=C.run_frame(B);B.f_back=A;return D
	def run_code(A,code,f_globals=A,f_locals=A):
		B=A.make_frame(code,f_globals=f_globals,f_locals=f_locals);C=A.run_frame(B)
		if A.frames:raise L('Frames left over!')
		if A.frame and A.frame.stack:raise L('Data left on stack! %r'%A.frame.stack)
		return C
	def unwind_block(A,block):
		B=block
		if B.type==P:C=3
		else:C=0
		while J(A.frame.stack)>B.level+C:A.pop()
		if B.type==P:D,E,F=A.popn(3);A.last_exception=F,E,D
	def parse_byte_and_args(K):
		' Parse 1 - 3 bytes of bytecode into\n        an instruction and optionally arguments.\n        In Python3.6 the format is 2 bytes per instruction.';B=K.frame;H=B.f_lasti
		if D.version_info>=(3,6):I=B.opcodes[H];F=I.opcode;L=I.opname
		else:F=U(B.f_code.co_code[H]);L=G.opname[F]
		B.f_lasti+=1;C=A;M=[]
		if D.version_info>=(3,6)and F==G.EXTENDED_ARG:return K.parse_byte_and_args()
		if F>=G.HAVE_ARGUMENT:
			if D.version_info>=(3,6):E=I.arg
			else:C=B.f_code.co_code[B.f_lasti:B.f_lasti+2];B.f_lasti+=2;E=U(C[0])+(U(C[1])<<8)
			if F in G.hasconst:C=B.f_code.co_consts[E]
			elif F in G.hasfree:
				if E<J(B.f_code.co_cellvars):C=B.f_code.co_cellvars[E]
				else:N=E-J(B.f_code.co_cellvars);C=B.f_code.co_freevars[N]
			elif F in G.hasname:C=B.f_code.co_names[E]
			elif F in G.hasjrel:
				if D.version_info>=(3,6):C=B.f_lasti+E//2
				else:C=B.f_lasti+E
			elif F in G.hasjabs:
				if D.version_info>=(3,6):C=E//2
				else:C=E
			elif F in G.haslocal:C=B.f_code.co_varnames[E]
			else:C=E
			M=[C]
		return L,M,H
	def log(A,byteName,arguments,opoffset):
		' Log arguments, block stack, and data stack for each opcode.';C=arguments;D='%d: %s'%(opoffset,byteName)
		if C:D+=' %r'%(C[0],)
		B=AB*(J(A.frames)-1);E=a(A.frame.stack);F=a(A.frame.block_stack);log.info('  %sdata: %s'%(B,E));log.info('  %sblks: %s'%(B,F));log.info('%s%s'%(B,D))
	def dispatch(C,byteName,arguments):
		' Dispatch by bytename to the corresponding methods.\n        Exceptions are caught and set on the virtual machine.';B=byteName;E=A
		try:
			if B.startswith('UNARY_'):C.unaryOperator(B[6:])
			elif B.startswith('BINARY_'):C.binaryOperator(B[7:])
			elif B.startswith('INPLACE_'):C.inplaceOperator(B[8:])
			elif'SLICE+'in B:C.sliceOperator(B)
			else:
				F=X(C,'byte_%s'%B,A)
				if not F:raise L('unknown bytecode type: %s'%B)
				E=F(*arguments)
		except:C.last_exception=D.exc_info()[:2]+(A,);log.exception('Caught exception during execution');E=H
		return E
	def manage_block_stack(B,why):
		" Manage a frame's block stack.\n        Manipulate the block stack and data stack for looping,\n        exception handling, or returning.";C=why;assert C!=d;D=B.frame.block_stack[-1]
		if D.type==q and C==Q:B.jump(B.return_value);C=A;return C
		B.pop_block();B.unwind_block(D)
		if D.type==q and C==AC:C=A;B.jump(D.handler);return C
		if K:
			if D.type==Z or D.type==r and C==H or D.type==AD:
				if C==H:F,G,I=B.last_exception;B.push(I,G,F)
				else:
					if C in(R,Q):B.push(B.return_value)
					B.push(C)
				C=A;B.jump(D.handler);return C
		elif E:
			if C==H and D.type in[r,Z]:B.push_block(P);F,G,I=B.last_exception;B.push(I,G,F);B.push(I,G,F);C=A;B.jump(D.handler);return C
			elif D.type==Z:
				if C in(R,Q):B.push(B.return_value)
				B.push(C);C=A;B.jump(D.handler);return C
		return C
	def run_frame(B,frame):
		'Run a frame until it returns (somehow).\n\n        Exceptions are raised, the return value is returned.\n\n        ';C=frame;B.push_frame(C)
		while p:
			D,E,F=B.parse_byte_and_args()
			if log.isEnabledFor(h.INFO):B.log(D,E,F)
			A=B.dispatch(D,E)
			if A==H:0
			if A==e:A=H
			if A!=d:
				while A and C.block_stack:A=B.manage_block_stack(A)
			if A:break
		B.pop_frame()
		if A==H:I.reraise(*B.last_exception)
		return B.return_value
	def byte_LOAD_CONST(A,const):A.push(const)
	def byte_POP_TOP(A):A.pop()
	def byte_DUP_TOP(A):A.push(A.top())
	def byte_DUP_TOPX(A,count):
		B=A.popn(count)
		for C in [1,2]:A.push(*B)
	def byte_DUP_TOP_TWO(A):B,C=A.popn(2);A.push(B,C,B,C)
	def byte_ROT_TWO(A):B,C=A.popn(2);A.push(C,B)
	def byte_ROT_THREE(A):B,C,D=A.popn(3);A.push(D,B,C)
	def byte_ROT_FOUR(A):B,C,D,E=A.popn(4);A.push(E,B,C,D)
	def byte_LOAD_NAME(D,name):
		A=name;B=D.frame
		if A in B.f_locals:C=B.f_locals[A]
		elif A in B.f_globals:C=B.f_globals[A]
		elif A in B.f_builtins:C=B.f_builtins[A]
		else:raise o(AE%A)
		D.push(C)
	def byte_STORE_NAME(A,name):A.frame.f_locals[name]=A.pop()
	def byte_DELETE_NAME(A,name):del A.frame.f_locals[name]
	def byte_LOAD_FAST(A,name):
		B=name
		if B in A.frame.f_locals:C=A.frame.f_locals[B]
		else:raise UnboundLocalError("local variable '%s' referenced before assignment"%B)
		A.push(C)
	def byte_STORE_FAST(A,name):A.frame.f_locals[name]=A.pop()
	def byte_DELETE_FAST(A,name):del A.frame.f_locals[name]
	def byte_LOAD_GLOBAL(C,name):
		A=name;B=C.frame
		if A in B.f_globals:D=B.f_globals[A]
		elif A in B.f_builtins:D=B.f_builtins[A]
		elif K:raise o("global name '%s' is not defined"%A)
		elif E:raise o(AE%A)
		C.push(D)
	def byte_STORE_GLOBAL(A,name):B=A.frame;B.f_globals[name]=A.pop()
	def byte_LOAD_DEREF(A,name):A.push(A.frame.cells[name].get())
	def byte_STORE_DEREF(A,name):A.frame.cells[name].set(A.pop())
	def byte_LOAD_LOCALS(A):A.push(A.frame.f_locals)
	UNARY_OPERATORS={'POSITIVE':B.pos,'NEGATIVE':B.neg,'NOT':B.not_,'CONVERT':repr,'INVERT':B.invert}
	def unaryOperator(A,op):B=A.pop();A.push(A.UNARY_OPERATORS[op](B))
	BINARY_OPERATORS={AF:pow,AG:B.mul,AH:X(B,'div',lambda x,y:A),AI:B.floordiv,AJ:B.truediv,AK:B.mod,AL:B.add,AM:B.sub,'SUBSCR':B.getitem,AN:B.lshift,AO:B.rshift,AP:B.and_,AQ:B.xor,'OR':B.or_}
	def binaryOperator(A,op):B,C=A.popn(2);A.push(A.BINARY_OPERATORS[op](B,C))
	def inplaceOperator(D,op):
		A=op;B,C=D.popn(2)
		if A==AF:B**=C
		elif A==AG:B*=C
		elif A in[AH,AI]:B//=C
		elif A==AJ:B/=C
		elif A==AK:B%=C
		elif A==AL:B+=C
		elif A==AM:B-=C
		elif A==AN:B<<=C
		elif A==AO:B>>=C
		elif A==AP:B&=C
		elif A==AQ:B^=C
		elif A=='OR':B|=C
		else:raise L('Unknown in-place operator: %r'%A)
		D.push(B)
	def sliceOperator(B,op):
		D=op;E=0;C=A;D,G=D[:-2],int(D[-1])
		if G==1:E=B.pop()
		elif G==2:C=B.pop()
		elif G==3:C=B.pop();E=B.pop()
		F=B.pop()
		if C is A:C=J(F)
		if D.startswith('STORE_'):F[E:C]=B.pop()
		elif D.startswith('DELETE_'):del F[E:C]
		else:B.push(F[E:C])
	COMPARE_OPERATORS=[B.lt,B.le,B.eq,B.ne,B.gt,B.ge,lambda x,y:x in y,lambda x,y:x not in y,lambda x,y:x is y,lambda x,y:x is not y,lambda x,y:N(x,n)and N(x,y)]
	def byte_COMPARE_OP(A,opnum):B,C=A.popn(2);A.push(A.COMPARE_OPERATORS[opnum](B,C))
	def byte_LOAD_ATTR(A,attr):B=A.pop();C=X(B,attr);A.push(C)
	def byte_STORE_ATTR(A,name):B,C=A.popn(2);setattr(C,name,B)
	def byte_DELETE_ATTR(A,name):B=A.pop();delattr(B,name)
	def byte_STORE_SUBSCR(A):B,C,D=A.popn(3);C[D]=B
	def byte_DELETE_SUBSCR(A):B,C=A.popn(2);del B[C]
	def byte_BUILD_TUPLE_UNPACK_WITH_CALL(A,count):A.build_container_flat(count,V)
	def byte_BUILD_TUPLE_UNPACK(A,count):A.build_container_flat(count,V)
	def byte_BUILD_TUPLE(A,count):A.build_container(count,V)
	def byte_BUILD_LIST_UNPACK(A,count):A.build_container_flat(count,list)
	def byte_BUILD_SET_UNPACK(A,count):A.build_container_flat(count,set)
	def byte_BUILD_MAP_UNPACK(A,count):A.build_container(count,c)
	def byte_BUILD_MAP_UNPACK_WITH_CALL(A,count):A.build_container(count,c)
	def build_container_flat(A,count,container_fn):B=A.popn(count);A.push(container_fn((C for A in B for C in A)))
	def build_container(A,count,container_fn):B=A.popn(count);A.push(container_fn(B))
	def byte_BUILD_LIST(A,count):B=A.popn(count);A.push(B)
	def byte_BUILD_SET(A,count):B=A.popn(count);A.push(set(B))
	def byte_BUILD_CONST_KEY_MAP(A,count):B=A.pop();C=A.popn(count);D=c(b(B,C));A.push(D)
	def byte_BUILD_MAP(A,count):
		if D.version_info<(3,5):A.push({});return
		B={}
		for F in A5(count):C,E=A.popn(2);B[C]=E
		A.push(B)
	def byte_STORE_MAP(A):B,C,D=A.popn(3);B[D]=C;A.push(B)
	def byte_UNPACK_SEQUENCE(A,count):
		B=A.pop()
		for C in reversed(B):A.push(C)
	def byte_BUILD_SLICE(A,count):
		B=count
		if B==2:C,D=A.popn(2);A.push(A6(C,D))
		elif B==3:C,D,E=A.popn(3);A.push(A6(C,D,E))
		else:raise L('Strange BUILD_SLICE count: %r'%B)
	def byte_LIST_APPEND(A,count):B=A.pop();C=A.peek(count);C.append(B)
	def byte_SET_ADD(A,count):B=A.pop();C=A.peek(count);C.add(B)
	def byte_MAP_ADD(A,count):B,C=A.popn(2);D=A.peek(count);D[C]=B
	if 0:
		def byte_PRINT_EXPR(A):M(A.pop())
	def byte_PRINT_ITEM(A):B=A.pop();A.print_item(B)
	def byte_PRINT_ITEM_TO(A):B=A.pop();C=A.pop();A.print_item(C,B)
	def byte_PRINT_NEWLINE(A):A.print_newline()
	def byte_PRINT_NEWLINE_TO(A):B=A.pop();A.print_newline(B)
	def print_item(G,item,to=A):
		F=' ';E=item;B=to
		if B is A:B=D.stdout
		if B.softspace:M(F,end=f,file=B);B.softspace=0
		M(E,end=f,file=B)
		if C(E,Y):
			if not E or not E[-1].isspace()or E[-1]==F:B.softspace=1
		else:B.softspace=1
	def print_newline(B,to=A):
		if to is A:to=D.stdout
		M(f,file=to);to.softspace=0
	def byte_JUMP_FORWARD(A,jump):A.jump(jump)
	def byte_JUMP_ABSOLUTE(A,jump):A.jump(jump)
	if 0:
		def byte_JUMP_IF_TRUE(A,jump):
			B=A.top()
			if B:A.jump(jump)
		def byte_JUMP_IF_FALSE(A,jump):
			B=A.top()
			if not B:A.jump(jump)
	def byte_POP_JUMP_IF_TRUE(A,jump):
		B=A.pop()
		if B:A.jump(jump)
	def byte_POP_JUMP_IF_FALSE(A,jump):
		B=A.pop()
		if not B:A.jump(jump)
	def byte_JUMP_IF_TRUE_OR_POP(A,jump):
		B=A.top()
		if B:A.jump(jump)
		else:A.pop()
	def byte_JUMP_IF_FALSE_OR_POP(A,jump):
		B=A.top()
		if not B:A.jump(jump)
		else:A.pop()
	def byte_SETUP_LOOP(A,dest):A.push_block(q,dest)
	def byte_GET_ITER(A):A.push(iter(A.pop()))
	def byte_GET_YIELD_FROM_ITER(B):
		A=B.top()
		if C(A,S.GeneratorType)or C(A,S.CoroutineType):return
		A=B.pop();B.push(iter(A))
	def byte_FOR_ITER(A,jump):
		B=A.top()
		try:C=next(B);A.push(C)
		except m:A.pop();A.jump(jump)
	def byte_BREAK_LOOP(A):return AC
	def byte_CONTINUE_LOOP(A,dest):A.return_value=dest;return Q
	def byte_SETUP_EXCEPT(A,dest):A.push_block(r,dest)
	def byte_SETUP_FINALLY(A,dest):A.push_block(Z,dest)
	def byte_END_FINALLY(B):
		E=B.pop()
		if C(E,Y):
			D=E
			if D in(R,Q):B.return_value=B.pop()
			if D==s:F=B.pop_block();assert F.type==P;B.unwind_block(F);D=A
		elif E is A:D=A
		elif N(E,O):G=E;H=B.pop();I=B.pop();B.last_exception=G,H,I;D=e
		else:raise L('Confused END_FINALLY')
		return D
	def byte_POP_BLOCK(A):A.pop_block()
	if K:
		def byte_RAISE_VARARGS(B,argc):
			G=argc;D=E=I=A
			if G==0:D,E,I=B.last_exception
			elif G==1:D=B.pop()
			elif G==2:E=B.pop();D=B.pop()
			elif G==3:I=B.pop();E=B.pop();D=B.pop()
			if C(D,O):E=D;D=F(E)
			B.last_exception=D,E,I
			if I:return e
			else:return H
	elif E:
		def byte_RAISE_VARARGS(B,argc):
			D=C=A
			if argc==2:D=B.pop();C=B.pop()
			elif argc==1:C=B.pop()
			return B.do_raise(C,D)
		def do_raise(I,exc,cause):
			D=cause;B=exc
			if B is A:
				G,E,J=I.last_exception
				if G is A:return H
				else:return e
			elif F(B)==F:G=B;E=B()
			elif C(B,O):G=F(B);E=B
			else:return H
			if D:
				if F(D)==F:D=D()
				elif not C(D,O):return H
				E.__cause__=D
			I.last_exception=G,E,E.__traceback__;return H
	def byte_POP_EXCEPT(A):
		B=A.pop_block()
		if B.type!=P:raise n('popped block is not an except handler')
		A.unwind_block(B)
	def byte_SETUP_WITH(A,dest):
		B=A.pop();A.push(B.__exit__);C=B.__enter__()
		if K:A.push_block(AD,dest)
		elif E:A.push_block(Z,dest)
		A.push(C)
	def byte_WITH_CLEANUP_START(B):
		D=B.top();G=A;H=A
		if D is A:E=B.pop(1)
		elif C(D,Y):
			if D in{R,Q}:E=B.pop(2)
			else:E=B.pop(1)
		elif N(D,O):H,G,D=B.popn(3);I,J,K=B.popn(3);E=B.pop();B.push(I,J,K);B.push(A);B.push(H,G,D);F=B.pop_block();assert F.type==P;B.push_block(F.type,F.handler,F.level-1)
		L=E(D,G,H);B.push(D);B.push(L)
	def byte_WITH_CLEANUP_FINISH(A):
		C=A.pop();B=A.pop()
		if F(B)is F and N(B,O)and C:A.push(s)
	def byte_WITH_CLEANUP(B):
		F=G=A;D=B.top()
		if D is A:H=B.pop(1)
		elif C(D,Y):
			if D in(R,Q):H=B.pop(2)
			else:H=B.pop(1)
			D=A
		elif N(D,O):
			if K:G,F,D=B.popn(3);H=B.pop();B.push(G,F,D)
			elif E:G,F,D=B.popn(3);J,M,S=B.popn(3);H=B.pop();B.push(J,M,S);B.push(A);B.push(G,F,D);I=B.pop_block();assert I.type==P;B.push_block(I.type,I.handler,I.level-1)
		else:raise L('Confused WITH_CLEANUP')
		T=H(D,F,G);U=D is not A and bool(T)
		if U:
			if K:B.popn(3);B.push(A)
			elif E:B.push(s)
	def byte_MAKE_FUNCTION(B,argc):
		C=argc
		if E:F=B.pop()
		else:F=A
		H=B.pop();I=B.frame.f_globals
		if E and D.version_info.minor>=6:K=B.pop()if C&8 else A;M=B.pop()if C&4 else A;L=B.pop()if C&2 else A;G=B.pop()if C&1 else A;J=T(F,H,I,G,L,K,B)
		else:G=B.popn(C);J=T(F,H,I,G,A,A,B)
		B.push(J)
	def byte_LOAD_CLOSURE(A,name):A.push(A.frame.cells[name])
	def byte_MAKE_CLOSURE(B,argc):
		if E:C=B.pop()
		else:C=A
		D,F=B.popn(2);G=B.popn(argc);H=B.frame.f_globals;I=T(C,F,H,G,A,D,B);B.push(I)
	def byte_CALL_FUNCTION_EX(A,arg):B=A.pop()if arg&1 else{};C=A.pop();return A.call_function(0,C,B)
	def byte_CALL_FUNCTION(A,arg):return A.call_function(arg,[],{})
	def byte_CALL_FUNCTION_VAR(A,arg):B=A.pop();return A.call_function(arg,B,{})
	def byte_CALL_FUNCTION_KW(A,argc):
		if not(I.PY3 and D.version_info.minor>=6):B=A.pop();return A.call_function(argc,[],B)
		C=A.pop();E=J(C);B=A.popn(E);F=argc-E;return A.call_function(F,[],c(b(C,B)))
	def byte_CALL_FUNCTION_VAR_KW(A,arg):B,C=A.popn(2);return A.call_function(arg,B,C)
	def call_function(B,arg,args,kwargs):
		G,H=divmod(arg,256);E={}
		for L in A5(G):I,J=B.popn(2);E[I]=J
		E.update(kwargs);D=B.popn(H);D.extend(args);A=B.pop();M=B.frame
		if A4(A,'im_func'):
			if A.im_self:D.insert(0,A.im_self)
			if not C(D[0],A.im_class):raise W('unbound method %s() must be called with %s instance as first argument (got %s instance instead)'%(A.im_func.func_name,A.im_class.__name__,F(D[0]).__name__))
			A=A.im_func
		K=A(*D,**E);B.push(K)
	def byte_RETURN_VALUE(A):
		A.return_value=A.pop()
		if A.frame.generator:A.frame.generator.finished=p
		return R
	def byte_YIELD_VALUE(A):A.return_value=A.pop();return d
	def byte_YIELD_FROM(B):
		E=B.pop();D=B.top()
		try:
			if not C(D,k)or E is A:F=next(D)
			else:F=D.send(E)
			B.return_value=F
		except m as G:B.pop();B.push(G.value)
		else:B.jump(B.frame.f_lasti-1);return d
	def byte_IMPORT_NAME(A,name):C,D=A.popn(2);B=A.frame;A.push(__import__(name,B.f_globals,B.f_locals,D,C))
	def byte_IMPORT_STAR(B):
		C=B.pop()
		for A in dir(C):
			if A[0]!='_':B.frame.f_locals[A]=X(C,A)
	def byte_IMPORT_FROM(A,name):B=A.top();A.push(X(B,name))
	def byte_EXEC_STMT(A):B,C,D=A.popn(3);I.exec_(B,C,D)
	if K:
		def byte_BUILD_CLASS(A):B,C,D=A.popn(3);A.push(F(B,C,D))
	elif E:
		def byte_LOAD_BUILD_CLASS(A):A.push(A1)
		def byte_STORE_LOCALS(A):A.frame.f_locals=A.pop()
	if 0:
		def byte_SET_LINENO(A,lineno):A.frame.f_lineno=lineno
if E:
	def A1(func,name,*E,**I):
		'Like __build_class__ in bltinmodule.c, but running in the byterun VM.';G=name;D=func
		if not C(D,T):raise W('func must be a function')
		if not C(G,Y):raise W('name is not a string')
		B=I.pop('metaclass',A)
		if B is A:B=F(E[0])if E else F
		if C(B,F):B=A2(B,E)
		try:L=B.__prepare__
		except AttributeError:H={}
		else:H=L(G,E,**I)
		M=D._vm.make_frame(D.func_code,f_globals=D.func_globals,f_locals=H,f_closure=D.func_closure);J=D._vm.run_frame(M);K=B(G,E,H)
		if C(J,j):J.set(K)
		return K
	def A2(metaclass,bases):
		'Determine the most derived metatype.';A=metaclass
		for C in bases:
			B=F(C)
			if N(B,A):A=B
			elif not N(A,B):raise W('metaclass conflict',A,B)
		return A
class A3:
	def __init__(B):A=u.dedent('    HW = "Hello World!\\n"\n    print(HW * (len(HW) - 3))\n    ');A=compile(A,'main.py','exec');B.dis_code(A);D=I.StringIO();C=A0();C.run_code(A)
	def dis_code(D,code):
		'Disassemble `code` and all the code it refers to.';A=code
		for B in A.co_consts:
			if C(B,S.CodeType):D.dis_code(B)
		M(f);M(A);G.dis(A)
AR=A3()
