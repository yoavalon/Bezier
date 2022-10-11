d = DslBezier()

d.position_pen(1,2)
d.position_pen(2,2)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)

d.end()
