d = DslBezier()

d.position_pen(2,2)
d.position_pen(0,0)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.position_pen(2,2)
d.curve(Direction.NW, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.position_pen(2,3)

d.end()
