d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
