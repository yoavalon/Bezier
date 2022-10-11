d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,1)

d.end()
