d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.NE, Orient.right, Length.long, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.position_pen(0,2)
d.straight_line(Direction.S, Length.medium)

d.end()
