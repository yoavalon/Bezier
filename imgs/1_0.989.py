d = DslBezier()

d.position_pen(3,3)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.S, Length.long)
d.position_pen(1,2)
d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)

d.end()
