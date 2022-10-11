d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)
d.position_pen(2,3)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(1,2)
d.straight_line(Direction.NW, Length.long)

d.end()
