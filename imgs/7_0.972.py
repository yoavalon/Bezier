d = DslBezier()

d.position_pen(3,2)
d.position_pen(1,2)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.short)
d.position_pen(2,0)

d.end()
