d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.W, Length.long)
d.position_pen(2,0)
d.curve(Direction.NE, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.NE, Length.short)

d.end()
