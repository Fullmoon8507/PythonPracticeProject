#######################################################
# 【スコープの考え方（LEGBルール）】
# 1.ローカルスコープ    ：Local Scope
# 2.外側の関数のスコープ：Enclosing Function's Scope
# 3.グローバルスコープ  ：Global Scope
# 4.ビルトインスコープ  ：Built-in Scope
#######################################################

variable = 33           # Global Scope

def func():
    variable = 22       # Enclosing Function's Scope

    print(variable)

    def func():
        variable = 11   # Local Scope

        print(variable)

    return func

print(__name__)         # show builtin variable:__main__
print(variable)         # show global variable:33
f = func()              # show enclosing function's scope variable:22
f()                     # show local variable:11
