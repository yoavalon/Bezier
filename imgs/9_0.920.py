d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.N, Orient.right, Length.long, Radius.medium)
d.position_pen(0,3)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.position_pen(1,3)

d.end()
