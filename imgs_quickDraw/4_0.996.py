d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.SE, Orient.left, Length.short, Radius.low)
d.position_pen(0,3)

d.end()
