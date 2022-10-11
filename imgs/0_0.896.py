d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.curve(Direction.N, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.NE, Length.short)
d.position_pen(1,2)
d.straight_line(Direction.SE, Length.long)

d.end()
