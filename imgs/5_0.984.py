d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)

d.end()
