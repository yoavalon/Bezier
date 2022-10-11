d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.long)
d.position_pen(2,2)

d.end()
