d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.N, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,0)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,1)

d.end()
