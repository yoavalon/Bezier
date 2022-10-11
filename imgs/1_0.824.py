d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NE, Length.long)
d.position_pen(2,3)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)

d.end()
