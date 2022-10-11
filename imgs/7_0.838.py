d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.low)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.short)
d.position_pen(2,3)

d.end()
