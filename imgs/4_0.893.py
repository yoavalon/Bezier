d = DslBezier()

d.position_pen(3,2)
d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,0)

d.end()
