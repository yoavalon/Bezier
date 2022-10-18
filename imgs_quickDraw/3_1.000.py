d = DslBezier()

d.position_pen(3,0)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,1)

d.end()
