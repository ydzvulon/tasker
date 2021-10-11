
class _if:

    def __init__(self, condition):
        self.condition_ = condition

    def _then(self, expr):
        self.then_ = expr

    def _else(self, expr):
        self.else_ = expr

    def _elif(self, expr):
        self._elif = expr

    def __call__(self, *args, **kwargs):
        if self.condition_:
            res = self.then_(self.con)
        else:
            res = self.else_()
        return res

#_if(lambda bama: bama  < 10).then_(lambda bama: bama + 8)
# with expr(ba)