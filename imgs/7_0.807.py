d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.long, Radius.low)
d.position_pen(1,3)
d.straight_line(Direction.SW, Length.short)

d.end()
