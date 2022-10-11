d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.W, Orient.right, Length.short, Radius.low)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,1)

d.end()
