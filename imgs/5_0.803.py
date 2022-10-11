d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.position_pen(2,3)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)

d.end()
