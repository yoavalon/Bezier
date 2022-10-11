d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.E, Length.medium)
d.position_pen(1,3)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)

d.end()
