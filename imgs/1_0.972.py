d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.E, Length.medium)
d.position_pen(3,2)
d.curve(Direction.S, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,0)

d.end()
