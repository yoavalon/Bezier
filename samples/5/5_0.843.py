d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,3)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)

d.end()
