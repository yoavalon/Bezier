d = DslBezier()

d.position_pen(1,1)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)

d.end()
