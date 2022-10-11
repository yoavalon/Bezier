d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.position_pen(1,2)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.long, Radius.low)

d.end()
