d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.position_pen(1,0)
d.straight_line(Direction.W, Length.short)
d.position_pen(3,1)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)

d.end()
