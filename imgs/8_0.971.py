d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.position_pen(1,1)
d.straight_line(Direction.NE, Length.long)
d.position_pen(1,2)

d.end()
