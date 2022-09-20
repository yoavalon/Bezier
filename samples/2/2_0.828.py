d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.NE, Length.medium)

d.end()
