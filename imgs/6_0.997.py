d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.short)
d.position_pen(2,3)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)

d.end()
