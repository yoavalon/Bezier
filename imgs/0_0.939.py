d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,1)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.position_pen(1,3)
d.straight_line(Direction.NW, Length.medium)

d.end()
