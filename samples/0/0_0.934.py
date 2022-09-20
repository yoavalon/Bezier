d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.position_pen(0,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.position_pen(0,2)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)

d.end()
