d = DslBezier()

d.position_pen(1,1)
d.position_pen(1,0)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.position_pen(2,2)
d.straight_line(Direction.NE, Length.medium)

d.end()
