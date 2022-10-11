d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)

d.end()
