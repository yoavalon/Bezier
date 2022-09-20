d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NE, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.SE, Length.short)
d.position_pen(1,3)

d.end()
