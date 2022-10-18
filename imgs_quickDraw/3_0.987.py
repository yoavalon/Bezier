d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)
d.position_pen(3,0)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,2)

d.end()
